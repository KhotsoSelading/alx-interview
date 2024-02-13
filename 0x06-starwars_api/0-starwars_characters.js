#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
  let response = await request(endpoint);
  response = JSON.parse(response.body);
  const characters = response.characters;

  const characterRequests = characters.map(url => request(url));
  const characterResponses = await Promise.all(characterRequests);
  const characterData = characterResponses.map(res => JSON.parse(res.body));

  characterData.forEach(character => {
    console.log(character.name);
  });
}

starwarsCharacters(filmID);
