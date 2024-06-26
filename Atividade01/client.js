const net = require('net');
const fs = require('fs');
const path = require('path');

const PASTA_ARQUIVOS = 'arquivos';
let ip;
let porta;
let nomeArquivo;
const url = "http://127.0.0.1:8088/teste.html"
const urlParts = url.split('/');
ip = urlParts[2].split(':')[0];
porta = urlParts[2].split(':')[1];
nomeArquivo = urlParts[3];

const cliente = net.createConnection({
  host: ip,
  port: porta
});

cliente.write(nomeArquivo);

// tamanhoArquivo
cliente.on('data', (data) => {
  const tamanhoArquivo = parseInt(data.toString());

  if (!fs.existsSync(PASTA_ARQUIVOS)) {
    fs.mkdirSync(PASTA_ARQUIVOS);
  }

  const arquivo = fs.createWriteStream(path.join(PASTA_ARQUIVOS, nomeArquivo));

  let recebido = 0;
  cliente.on('data', (buffer) => {
    arquivo.write(buffer);
    recebido += buffer.length;

    if (recebido === tamanhoArquivo) {
      cliente.end();

      fs.readFile('./arquivos/teste.html', 'utf8', (err, data) => {
        if (err) {
          console.error(err);
          return;
        }
        console.log(data);
      });

      arquivo.close();
    }
  });
});
