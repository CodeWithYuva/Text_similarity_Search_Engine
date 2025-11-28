const btn = document.getElementById('btn');
const qEl = document.getElementById('query');
const resultsEl = document.getElementById('results');
const fileInput = document.getElementById('fileInput');

loadHistory();

btn.addEventListener('click', async () => { await doSearch(); });

async function doSearch() {
  const query = qEl.value.trim();
  resultsEl.innerHTML = '';


  const resp = await fetch('/search', {
    method: 'POST',
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ query })
  });

  const data = await resp.json();
 


  data.results.forEach((r,i)=>{
    console.log(r);
    resultsEl.innerHTML += `
      <div class="result">
        <b>#${i+1} (${r.score})</b><br>
        ${r.sentence_html}
      </div>
    `;
  });

  saveHistory(query);
  loadHistory();
}

// Upload dataset
fileInput.addEventListener('change', async e => {
  const text = await e.target.files[0].text();
  await fetch("/upload-dataset", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ data: text })
  });
});

// History (localStorage)
function saveHistory(q){
  let h = JSON.parse(localStorage.getItem("history") || "[]");
  h.unshift({query:q, time:new Date().toLocaleString()});
  localStorage.setItem("history", JSON.stringify(h.slice(0,20)));
}

function loadHistory(){
  let h = JSON.parse(localStorage.getItem("history") || "[]");
  const div = document.getElementById("history");
  div.innerHTML = h.map(x=>`<div>${x.query} <small>(${x.time})</small></div>`).join("");
}
