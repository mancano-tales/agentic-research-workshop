// Enquete da Sessão 1: formulário (survey/) e resultados (survey/results/).
// Depois de publicar tools/survey-backend.gs, cole a URL do app web em ENDPOINT.
// Para testar sem backend, abra qualquer uma das páginas com ?mock=1.
(function () {
  "use strict";

  const ENDPOINT = "https://script.google.com/macros/s/AKfycbwnXSzgE-8tb37sgBM7SYscbhG8h5BTXpITiXN9rvllBqmH5DkpmM7iR9xFoW4hCZlj/exec";
  const STORAGE_KEY = "enquete-sessao-1-respondida";
  const POLL_MS = 4000;
  const MAX_TRIES = 4;

  // Os códigos precisam ser iguais aos de QUESTIONS em tools/survey-backend.gs.
  const QUESTIONS = [
    {
      id: "chatbot",
      label: "Com que frequência você usa chatbots de IA na pesquisa?",
      options: [
        ["nunca", "Nunca"],
        ["testei", "Já testei"],
        ["semana", "Toda semana"],
        ["dia", "Quase todo dia"],
      ],
    },
    {
      id: "agente",
      label: "Já usou um agente que roda comandos ou edita arquivos no seu computador?",
      options: [
        ["nao_sei", "Não sei o que é"],
        ["nunca", "Sei o que é, mas nunca usei"],
        ["testei", "Já testei"],
        ["regular", "Uso regularmente"],
      ],
    },
    {
      id: "dados",
      label: "Já usou IA para classificar ou extrair dados que entraram em uma análise?",
      options: [
        ["sim", "Sim"],
        ["nao", "Não"],
        ["pretendo", "Ainda não, mas pretendo"],
      ],
    },
    {
      id: "preocupa",
      label: "O que mais preocupa você no uso de agentes na pesquisa?",
      options: [
        ["erros", "Erros difíceis de perceber"],
        ["sigilo", "Sigilo dos dados"],
        ["habilidades", "Perder habilidades"],
        ["custo", "Custo"],
        ["regras", "Regras de periódicos e ética"],
      ],
    },
  ];

  const MOCK = new URLSearchParams(window.location.search).get("mock") === "1";

  function el(tag, attrs, text) {
    const node = document.createElement(tag);
    Object.entries(attrs || {}).forEach(([key, value]) => node.setAttribute(key, value));
    if (text !== undefined) node.textContent = text;
    return node;
  }

  function alreadyAnswered() {
    if (MOCK && new URLSearchParams(window.location.search).get("reset") === "1") return false;
    try {
      return window.localStorage.getItem(STORAGE_KEY) === "1";
    } catch (error) {
      return false;
    }
  }

  function markAnswered() {
    try {
      window.localStorage.setItem(STORAGE_KEY, "1");
    } catch (error) {
      // Sem armazenamento local, o envio vale do mesmo jeito.
    }
  }

  function post(answers) {
    // text/plain evita a requisição preflight, que o Apps Script não atende.
    return fetch(ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "text/plain;charset=utf-8" },
      body: JSON.stringify(answers),
    }).then((response) => response.json());
  }

  // Com a sala inteira enviando ao mesmo tempo, um envio pode falhar por sobrecarga.
  // Tenta de novo sozinho, com espera crescente, antes de mostrar o erro.
  function send(answers, attempt) {
    if (MOCK) return new Promise((resolve) => setTimeout(() => resolve({ ok: true }), 300));
    if (!ENDPOINT) return Promise.reject(new Error("sem backend"));
    const tries = attempt || 1;
    const retry = () =>
      new Promise((resolve) => setTimeout(resolve, tries * 1500 + Math.random() * 1000)).then(() =>
        send(answers, tries + 1)
      );
    return post(answers).then(
      (result) => (!result.ok && result.error === "ocupado" && tries < MAX_TRIES ? retry() : result),
      (error) => {
        if (tries < MAX_TRIES) return retry();
        throw error;
      }
    );
  }

  function showThanks(root) {
    root.replaceChildren(
      el("p", { class: "survey-thanks" }, "Obrigado! Os resultados vão aparecer na tela da sala.")
    );
  }

  function buildForm(root) {
    if (alreadyAnswered()) {
      showThanks(root);
      return;
    }
    if (!ENDPOINT && !MOCK) {
      root.replaceChildren(el("p", { class: "survey-thanks" }, "A enquete ainda não está aberta."));
      return;
    }

    const form = el("form", { novalidate: "" });
    QUESTIONS.forEach((question) => {
      const fieldset = el("fieldset", { class: "survey-question" });
      fieldset.append(el("legend", {}, question.label));
      question.options.forEach(([value, text]) => {
        const label = el("label", { class: "survey-option" });
        label.append(el("input", { type: "radio", name: question.id, value: value }));
        label.append(el("span", {}, text));
        fieldset.append(label);
      });
      form.append(fieldset);
    });

    const button = el("button", { type: "submit", class: "survey-submit", disabled: "" }, "Enviar");
    const status = el("p", { class: "survey-status", role: "status" });
    form.append(button, status);

    function answers() {
      const data = new FormData(form);
      return Object.fromEntries(QUESTIONS.map((question) => [question.id, data.get(question.id)]));
    }

    form.addEventListener("change", () => {
      button.disabled = Object.values(answers()).some((value) => !value);
    });

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      button.disabled = true;
      status.textContent = "Enviando...";
      send(answers())
        .then((result) => {
          if (!result.ok) throw new Error(result.error || "erro");
          markAnswered();
          showThanks(root);
        })
        .catch((error) => {
          status.textContent =
            error.message === "encerrada"
              ? "A enquete já foi encerrada."
              : "Não foi possível enviar. Tente de novo.";
          button.disabled = error.message === "encerrada";
        });
    });

    root.replaceChildren(form);
  }

  function mockResults() {
    const counts = {};
    QUESTIONS.forEach((question) => {
      counts[question.id] = {};
      question.options.forEach(([value], index) => {
        counts[question.id][value] = 3 + ((index * 7 + question.id.length) % 13);
      });
    });
    const total = Object.values(counts.chatbot).reduce((sum, value) => sum + value, 0);
    return Promise.resolve({ ok: true, total: total, counts: counts });
  }

  function fetchResults() {
    if (MOCK) return mockResults();
    if (!ENDPOINT) return Promise.reject(new Error("sem backend"));
    return fetch(ENDPOINT).then((response) => response.json());
  }

  function percent(part, whole) {
    return whole ? Math.round((100 * part) / whole) : 0;
  }

  function renderResults(root, data) {
    const total = Number(data.total) || 0;
    const frag = document.createDocumentFragment();
    frag.append(el("p", { class: "results-total" }, total + (total === 1 ? " resposta" : " respostas")));

    QUESTIONS.forEach((question) => {
      const counts = data.counts[question.id] || {};
      const block = el("section", { class: "results-question" });
      block.append(el("h2", {}, question.label));
      question.options.forEach(([value, text]) => {
        const count = Number(counts[value]) || 0;
        const share = percent(count, total);
        const row = el("div", { class: "results-row" });
        row.append(el("span", { class: "results-label" }, text));
        const track = el("span", { class: "results-track" });
        const bar = el("span", { class: "results-bar" });
        bar.style.width = share + "%";
        track.append(bar);
        row.append(track, el("span", { class: "results-value" }, share + "%"));
        block.append(row);
      });
      frag.append(block);
    });

    const usedChatbot = total - (Number(data.counts.chatbot && data.counts.chatbot.nunca) || 0);
    const regularAgent = Number(data.counts.agente && data.counts.agente.regular) || 0;
    frag.append(
      el(
        "p",
        { class: "results-compare" },
        "Nesta sala: " + percent(usedChatbot, total) + "% já usaram chatbots e " +
          percent(regularAgent, total) + "% usam agentes regularmente. " +
          "Entre 1.260 cientistas sociais quantitativos: 81% e 20% (amostra não representativa)."
      )
    );
    root.replaceChildren(frag);
  }

  function startResults(root) {
    const status = document.getElementById("survey-results-status");
    function tick() {
      fetchResults()
        .then((data) => {
          if (!data.ok) throw new Error(data.error || "erro");
          renderResults(root, data);
          status.textContent = "";
        })
        .catch(() => {
          status.textContent = "Sem conexão com o backend. Tentando de novo...";
        });
    }
    tick();
    window.setInterval(tick, POLL_MS);
  }

  document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("survey-form");
    const results = document.getElementById("survey-results");
    if (form) buildForm(form);
    if (results) startResults(results);
  });
})();
