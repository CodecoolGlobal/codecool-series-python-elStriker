import {dataHandler} from "./data/dataHandler.js";

class orderingShows {
    constructor() {
        this.order = 'ASC';
    }

    initOrdering() {
        this.displayShows();
        this.addEventOnTitles();
    }

    async displayShows() {
        if (this.order === 'ASC') {
            this.order = 'DESC';
            const shows = await dataHandler.orderShows('DESC');
            this.createTableBody(shows);
        } else {
            this.order = 'ASC';
            const shows = await dataHandler.orderShows('ASC');
            this.createTableBody(shows);
        }
    }

    createTableBody(shows) {
        const tableBody = document.querySelector('.ordered-shows-table-body');
        this.removeTableRows();
        for (let show of shows) {
            const tableRow = document.createElement('tr');
            tableRow.innerHTML = `<td class="titles">${show.title}</td> <td>${show.rating}</td>`;
            tableBody.appendChild(tableRow);
        }
    }

    addEventOnTitles() {
        const title = document.querySelector('.order-title');
        title.addEventListener('click', () => this.displayShows());
    }

    removeTableRows() {
        const tableBodyRows = document.querySelectorAll('tbody tr');
        tableBodyRows.forEach(row => row.remove());
    }
}

function initOrder() {
    const ordering = new orderingShows();
    ordering.initOrdering();
}

initOrder();