(async () => {
    try {
        let res = await fetch('http://localhost:5000/database');
        let data = await res.json();
            let dbContainer = document.getElementById('db-visualization');
            data.items.forEach(element => {
                let divUsername = document.createElement('div');
                divUsername.innerText = element.email;
                dbContainer.appendChild(divUsername);
        
                let divEmail = document.createElement('div');
                divEmail.innerText = element.name;
                dbContainer.appendChild(divEmail);
        
                let divAge = document.createElement('div');
                divAge.innerText = element.major;
                dbContainer.appendChild(divAge);
        
                let divGpa = document.createElement('div');
                divGpa.innerText = element.year;
                dbContainer.appendChild(divGpa);
            });
        
            let transactionContainer = document.getElementById('transactions');
            data.transactions.forEach(element => {
                let div = document.createElement('div');
                div.innerText = element;
                transactionContainer.appendChild(div);
            });
    } catch { 
        document.body.innerHTML = '';
        let div = document.createElement('div')
        div.id = 'container'

        let errorText = document.createElement('div');
        errorText.id = 'error-text'
        errorText.innerText = 'An error has occured or the server is not running!\n \
                               Check if the server has started and once started refresh the page.\n \
                               If you are still getting an error please report it to the demo\'s repository.'
        div.appendChild(errorText)
        
        document.body.appendChild(div);
    }   

    let button = document.getElementById('refresh-button');
    button.addEventListener('click', () => { location.reload() });
})();
