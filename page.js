
// const res = await fetch("http://127.0.0.1:5000/ip");
// const json = await res.json();
// console.log(json);

const api_url =
    "http://127.0.0.1:5000/ip";

async function getapi(url) {

    const response = await fetch(url);

    var data = await response.json();
    console.log(data);
    if (response) {
        hideloader();
    }
    show(data);
}
getapi(api_url);

// function hideloader() {
//     document.getElementById('loading').style.display = 'none';
// }

    document.getElementById("employees").innerHTML = tab;
