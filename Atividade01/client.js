const net = require('net');
const fs = require('fs');
const path = require('path');

//servidor
const HOST = '127.0.0.1';
const PORT = 8088;

const PASTA_ARQUIVOS = 'arquivos';

const cliente = net.createConnection({
  host: HOST,
  port: PORT
});

const nomeArquivo = 'teste.html';
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
