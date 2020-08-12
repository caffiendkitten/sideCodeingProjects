'use strict';

const fetch = require('node-fetch');
const token = process.env.TOKEN;

module.exports = function(stocks) {
  if (!Array.isArray(stocks)) {
    return fetch(`https://cloud.iexapis.com/stable/stock/${stocks}/quote?token=${token}`).then(result =>
      result.json()
    );
  } else {
    return Promise.all([
      fetch(`https://cloud.iexapis.com/stable/stock/${stocks[0]}/quote?token=${token}`).then(result =>
        result.json()
      ),
      fetch(`https://cloud.iexapis.com/stable/stock/${stocks[1]}/quote?token=${token}`).then(result =>
        result.json()
      )
    ]);
  }
};
