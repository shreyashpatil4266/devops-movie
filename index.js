const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Welcome to the DevOps Movie Application!');
});

app.listen(port, () => {
  console.log(`App is running at http://localhost:${port}`);
});
#123
