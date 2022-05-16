export let dataHandler={
    getMostRatedShows: async function(){
        const response = await apiGet("/api/get-most-rated-shows");
        return response
    }
};

async function apiGet(url){
    let response = await fetch(url, {
        method: "GET",
    });
    if (response.status === 200){
        let data = response.json();
        return data
    }
}