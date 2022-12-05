const api_url =
    "http://127.0.0.1:5000/ip";

const freeip = [];
const blockip = [];

const getapi = async (url) => {
    const response = await fetch(url);
    
    const data = await response.json();
    data.forEach(row => {
        if (row[2] == 0)
            lockip.push(row);
        else
            freeip.push(row);
        
    })
}

const renderFreeIp = () => {
    const table = document.getElementById("test")
    
    freeip.forEach(element => {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${element[0]}</td><td>${element[1]}</td>`;
        table.appendChild(row)
    });
}
getapi(api_url).then(renderFreeIp);

function hideloader() {
    document.getElementById('loading').style.display = 'none';
}
