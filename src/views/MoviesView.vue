<script setup>
//Exercise 5
import {ref, onMounted} from "vue";

let movies = ref([]);

function fetchMovies(){
    fetch("/api/v1/movies", {method:'GET'})
    .then((response) => response.json())
    .then((data) => {//returns list of movies
        movies.value = data.data;})
    .catch((error) => {
      console.error("Error fetching movies:", error);
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<template>
    <div class="movies-container" v-if="movies.length">
        <h1>Movies</h1>
        <div class ="movies-grid">
            <div class="movie-card" v-for="movie in movies" :key="movie.id">
                <img :src="movie.poster" alt="Movie poster" />
                <div class="movie-info">
                    <h4>{{ movie.title }}</h4>
                    <p>{{ movie.description }}</p>
                </div>
            </div>
        </div>
    </div>
  <p v-else>No movies found.</p>
</template>

<style scoped>
.movies-container{
    padding:20px;
}

.movies-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-auto-rows: auto;
  gap: 20px;
  align-items: start;
}

.movie-card {
  display: flex;
  background-color: #f9f9f9;
  border: 1px solid #dcdcdc;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.movie-card img {
  width: 120px;
  height: auto;
  object-fit: cover;
}

.movie-info {
  padding: 10px;
  flex: 1;
}

.movie-info h3 {
  margin: 0;
  font-size: 16px;
}

.movie-info p {
  margin-top: 8px;
  font-size: 14px;
  color: black;
}
</style>