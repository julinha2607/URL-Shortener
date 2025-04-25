const form = document.getElementById('link-form');
const resultado = document.getElementById('resultado');

form.addEventListener('submit', async function (e) {
  e.preventDefault();

  const url = document.getElementById('url').value;

  const resposta = await fetch('/shorten', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url }),
  });

  const dados = await resposta.json();

  if (resposta.ok) {
    resultado.innerHTML = `
      <p>🔗 Link encurtado: 
        <a href="${dados.short_url}" target="_blank">${dados.short_url}</a>
      </p>`;
  } else {
    resultado.innerHTML = `<p style="color:red;">❌ Erro: ${dados.error}</p>`;
  }
});
