function deletePosts() {
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;
    const accessToken = document.getElementById('accessToken').value;
    const resultsDiv = document.getElementById('results');

    // Converti le date in timestamp UNIX
    const startTimestamp = new Date(startDate).getTime() / 1000;
    const endTimestamp = new Date(endDate).getTime() / 1000;

    // Qui dovresti inserire la logica per cancellare i post utilizzando l'API di Facebook.
    // Poiché il browser impedisce le richieste cross-origin dirette, considera di usare un server intermedio o le funzioni serverless.

    // Esempio fittizio di risultato
    resultsDiv.innerHTML = `Post cancellati tra ${startDate} e ${endDate}: X`;

    // Mostra un messaggio o i risultati qui
    console.log(`Cancellazione post da ${startTimestamp} a ${endTimestamp} con token ${accessToken}`);
}
