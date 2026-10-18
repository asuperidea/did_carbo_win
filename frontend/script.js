const URL = "https://did-carbo-win.vercel.app/";
const div = document.getElementById("yn");

async function getData(url){
    response = await fetch(url);
    const data = await response.json();

    if (data.win){
        div.innerHTML = '';
        div.innerHTML = `<h1 class="txt">YES</h1>`
    }
} 
(async () => {
    await getData(URL);
})();