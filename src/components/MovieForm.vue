<template>
    <!--Exercise 4-->
    <form @sumbit.prevent="saveMovie" id="movieForm">
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

        <button @click="submit">Submit</button>
    </form>
</template>

<script setup>

    function saveMovie(){
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm)
      

        fetch("/api/v1/movies", {method: 'POST', body:form_data})
        .then(function(response){
            return response.json();
        })
        .then(function(data){
            //display a success
            console.log('Movie added: ', data);
        })
        .catch(function(error){
            console.log(error);
        });
    }

</script>