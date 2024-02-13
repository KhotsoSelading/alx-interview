#!/usr/bin/node
const request = require('request-promise');
const movieId = process.argv[2];

async function printCharacters(movieId) {
  try {
    const film = await request({
      url: `https://swapi-api.hbtn.io/api/films/${movieId}`,
      json: true
    });

    for (const characterUrl of film.characters) {
      const character = await request({
        url: characterUrl,
        json: true
      });
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

printCharacters(movieId);
