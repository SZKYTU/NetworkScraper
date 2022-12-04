

const api_url =
    "http://127.0.0.1:5000/ip";

const freeip = [];
const blockip = [];

async function getapi(url) {

    const response = await fetch(url);

    const data = await response.json();
    // console.log(data);
    for (const status in data){
        if (data[status][2] == 0){
            blockip.push(data[status])
        } else{
            freeip.push(data[status])
        }
    }
}
getapi(api_url);

function hideloader() {
    document.getElementById('loading').style.display = 'none';
}

// function hideloader() {
//     document.getElementById('loading').style.display = 'none';
// }

function show(data) {
    let tab =
        `<tr>
          <th>ip</th>
          <th>hostname</th>
         </tr>`;

    for (let r of freeip.list) {
        tab += `<tr> 
    <td>${r.ip} </td>
    <td>${r.hn}</td>
</tr>`;
    }

console.log(freeip);
document.getElementById("test").innerHTML = tab;}