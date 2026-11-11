// Backend da enquete da Sessão 1 (Google Apps Script vinculado a uma planilha).
//
// Como publicar:
//   1. Crie uma planilha nova e abra Extensões > Apps Script.
//   2. Cole este arquivo no lugar do código existente e salve.
//   3. Implantar > Nova implantação > App da Web.
//      Executar como: Eu. Quem pode acessar: Qualquer pessoa.
//   4. Copie a URL terminada em /exec para ENDPOINT, em survey/survey.js.
//
// Só guarda data, hora e as quatro respostas. Depois da aula, rode encerrar().
// Antes de uma nova aplicação, rode limpar() e abrir().

const SHEET_NAME = "respostas";
const MAX_ROWS = 500;
const CACHE_SECONDS = 3;

// Os códigos precisam ser iguais aos de QUESTIONS em survey/survey.js.
const QUESTIONS = {
  chatbot: ["nunca", "testei", "semana", "dia"],
  agente: ["nao_sei", "nunca", "testei", "regular"],
  dados: ["sim", "nao", "pretendo"],
  preocupa: ["erros", "sigilo", "habilidades", "custo", "regras"],
};
const IDS = Object.keys(QUESTIONS);

function json_(payload) {
  return ContentService.createTextOutput(JSON.stringify(payload)).setMimeType(
    ContentService.MimeType.JSON
  );
}

function sheet_() {
  const book = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = book.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = book.insertSheet(SHEET_NAME);
    sheet.appendRow(["data_hora"].concat(IDS));
  }
  return sheet;
}

function isOpen_() {
  return PropertiesService.getScriptProperties().getProperty("ENCERRADA") !== "1";
}

function doPost(e) {
  let answers;
  try {
    answers = JSON.parse(e.postData.contents);
  } catch (error) {
    return json_({ ok: false, error: "formato" });
  }
  if (!isOpen_()) return json_({ ok: false, error: "encerrada" });

  const invalid = IDS.some((id) => QUESTIONS[id].indexOf(answers[id]) === -1);
  if (invalid) return json_({ ok: false, error: "resposta" });

  const lock = LockService.getScriptLock();
  try {
    lock.waitLock(15000);
  } catch (error) {
    return json_({ ok: false, error: "ocupado" });
  }
  try {
    const sheet = sheet_();
    if (sheet.getLastRow() > MAX_ROWS) return json_({ ok: false, error: "limite" });
    sheet.appendRow([new Date()].concat(IDS.map((id) => answers[id])));
  } finally {
    lock.releaseLock();
  }
  return json_({ ok: true });
}

function doGet() {
  const cache = CacheService.getScriptCache();
  const cached = cache.get("resultados");
  if (cached) return ContentService.createTextOutput(cached).setMimeType(ContentService.MimeType.JSON);

  const sheet = sheet_();
  const counts = {};
  IDS.forEach((id) => {
    counts[id] = {};
    QUESTIONS[id].forEach((value) => {
      counts[id][value] = 0;
    });
  });

  const rows = Math.max(sheet.getLastRow() - 1, 0);
  if (rows > 0) {
    sheet
      .getRange(2, 2, rows, IDS.length)
      .getValues()
      .forEach((row) => {
        IDS.forEach((id, index) => {
          if (counts[id][row[index]] !== undefined) counts[id][row[index]] += 1;
        });
      });
  }

  const body = JSON.stringify({ ok: true, total: rows, aberta: isOpen_(), counts: counts });
  cache.put("resultados", body, CACHE_SECONDS);
  return ContentService.createTextOutput(body).setMimeType(ContentService.MimeType.JSON);
}

function encerrar() {
  PropertiesService.getScriptProperties().setProperty("ENCERRADA", "1");
}

function abrir() {
  PropertiesService.getScriptProperties().deleteProperty("ENCERRADA");
}

function limpar() {
  const sheet = sheet_();
  const rows = sheet.getLastRow() - 1;
  if (rows > 0) sheet.deleteRows(2, rows);
}
