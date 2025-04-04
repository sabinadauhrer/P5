let persons = [];
let personId = 1;
let currentUserRole = null;

function checkEnter(event) {
    if (event.key === 'Enter') {
        login();
    }
}

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'admin' && password === 'admin123') {
        currentUserRole = 'admin';
        alert('Admin erfolgreich eingeloggt!');
        document.getElementById('loginSection').style.display = 'none';
        document.getElementById('adminForm').style.display = 'block';
        document.getElementById('dataTables').style.display = 'block';
        document.getElementById('searchSection').style.display = 'block';
    } else if (username === 'mitarbeiter' && password === 'mitarbeiter123') {
        currentUserRole = 'mitarbeiter';
        alert('Mitarbeiter erfolgreich eingeloggt!');
        document.getElementById('loginSection').style.display = 'none';
        document.getElementById('employeeForm').style.display = 'block';
        document.getElementById('dataTables').style.display = 'block';
        document.getElementById('searchSection').style.display = 'block';
    } else {
        alert('Ungültige Anmeldedaten!');
    }
}

function addEmployee() {
    if (currentUserRole !== 'admin') {
        alert('Nur Admins können Mitarbeiter hinzufügen!');
        return;
    }
    const firstName = document.getElementById('employeeFirstName').value;
    const lastName = document.getElementById('employeeLastName').value;
    const address = document.getElementById('employeeAddress').value;
    const email = document.getElementById('employeeEmail').value;
    const id = document.getElementById('employeeID').value;
    const iban = document.getElementById('employeeIBAN').value;

    if (firstName && lastName && address && email && id && iban) {
        persons.push({ id: personId++, firstName, lastName, address, email, type: 'Mitarbeiter', personID: id, iban });
        renderPersons();
    } else {
        alert('Bitte alle Felder ausfüllen!');
    }
}

function addCustomer() {
    if (currentUserRole !== 'mitarbeiter') {
        alert('Nur Mitarbeiter können Kunden hinzufügen!');
        return;
    }
    const firstName = document.getElementById('customerFirstName').value;
    const lastName = document.getElementById('customerLastName').value;
    const address = document.getElementById('customerAddress').value;
    const email = document.getElementById('customerEmail').value;
    const id = document.getElementById('customerID').value;
    const iban = document.getElementById('customerIBAN').value;

    if (firstName && lastName && address && email && id && iban) {
        persons.push({ id: personId++, firstName, lastName, address, email, type: 'Kunde', personID: id, iban });
        renderPersons();
    } else {
        alert('Bitte alle Felder ausfüllen!');
    }
}

function renderPersons() {
    const tableBody = document.getElementById('personTable').querySelector('tbody');
    tableBody.innerHTML = '';
    persons.forEach(person => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${person.id}</td>
            <td>${person.firstName}</td>
            <td>${person.lastName}</td>
            <td>${person.address}</td>
            <td>${person.email}</td>
            <td>${person.type}</td>
            <td>${person.personID}</td>
            <td>${person.iban}</td>
            <td>
                <span class="delete-btn" onclick="deletePerson(${person.id})">🗑️ Löschen</span>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

function deletePerson(id) {
    if (currentUserRole !== 'admin') {
        alert('Nur Admins können Personen löschen!');
        return;
    }
    persons = persons.filter(person => person.id !== id);
    renderPersons();
}

function filterPersons() {
    const searchValue = document.getElementById('searchInput').value.toLowerCase();
    const rows = document.querySelectorAll('#personTable tbody tr');

    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        const match = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(searchValue));
        row.style.display = match ? '' : 'none';
    });
}

function exportToPDF() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    doc.autoTable({ html: '#personTable' });
    doc.save('personenliste.pdf');
}
