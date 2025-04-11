<template>
    <!--Exercise 4-->
    <form @submit.prevent="saveMovie" id="movieForm">
        <div>
            <label for="title" class="form-label">Movie Title</label>
            <input type="text" name="title" class="form-control"/>
        </div>
        <div>
            <label for="description" class="form-label">Description</label>
            <textarea name="description" class="form-control"></textarea>
        </div>
        <div>
            <label for="poster" class="form-label">Photo Upload</label>
            <input type="file" name="poster" class="form-control" accept="image/*"/>
        </div>

        <button type="submit">Submit</button>
    </form>
</template>

<script setup>

import { ref, onMounted } from "vue";
let csrf_token = ref("");

function saveMovie(){
    const movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm)
      

    fetch("/api/v1/movies", {method: 'POST', body:form_data, headers: {
'X-CSRFToken': csrf_token.value}})
    .then((response) => response.json())
    .then((data) =>{
        //display a success
        console.log('Movie added: ', data)
    })
    .catch((error)=>console.log(error));
};

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })
}

onMounted(()=>{
    getCsrfToken();
});

</script>