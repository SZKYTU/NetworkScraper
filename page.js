const api_url =
"http://127.0.0.1:8000/ip";

const freeip = [];
const blockip = [];

const tableFREE = document.getElementById("free")
const tableBLOCK = document.getElementById("block")

const getapi = async (url) => {
    const response = await fetch(url);
    
    const data = await response.json();
    data.forEach(row => {
        if (row[2] == 0)
            blockip.push(row);
        else
            freeip.push(row);
        
    })
}

const render = (IP, table) => {

    IP.forEach(element => {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${element[0]}</td> -> <td>${element[1]}</td>`;
        table.appendChild(row)
    });
}

getapi(api_url).then(() =>{
    render(freeip, tableFREE)
    render(blockip, tableBLOCK)
});

function hideloader() {
    document.getElementById('loading').style.display = 'none';
}
