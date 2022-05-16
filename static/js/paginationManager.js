import {Pagination} from "./main.js";
import {dataHandler} from "./data/dataHandler.js";

export {initStart};


async function initStart() {
    const shows = await loadShows();
    const pagination = new Pagination(shows);
    pagination.initPagination();
}

async function loadShows(){
    const allShows = await dataHandler.getMostRatedShows();
    return allShows;
}

initStart();