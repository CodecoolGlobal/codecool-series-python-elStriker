export let dataHandler={
    getMostRatedShows: async function(){
        const response = await apiGet("/api/get-most-rated-shows");
        return response
    },

    getGenres: async function(){
        const response = await apiGet("/api/get-genres");
        return response
    },

    getGenresDetail: async function(genre_id){
        const response = await apiGet(`/api/get-genres-detail/${genre_id}`);
        return response
    },

    getActorsNshows: async function() {
        return await apiGet("/api/get-actors-detail")
    },

    orderShows: async function(order) {
        return await apiGet(`/api/get-ordered-shows/${order}`);
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