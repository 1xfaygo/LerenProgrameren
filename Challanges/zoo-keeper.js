//vraagt aantal dieren
aantal_giraffen = prompt("hoeveel giraffen zijn der:")
aantal_struisvogels = prompt("hoeveel struisvogels zijn der:")
aantal_zebras = prompt("hoeveel zebras zijn der:")


//de functie
function aantal_potten(aantal_giraffen, aantal_struisvogels, aantal_zebras) {
    const aantal_potten_giraffe = aantal_giraffen * 4;
    const aantal_potten_struisvogel = aantal_struisvogels * 2;
    const aantal_potten_zebras = aantal_zebras * 4;
    totale_potten = aantal_potten_zebras + aantal_potten_struisvogel + aantal_potten_giraffe;
    return totale_potten;
}
console.log(aantal_potten(aantal_giraffen,aantal_struisvogels,aantal_zebras));

