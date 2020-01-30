<template>
  <div>
    <form @submit.prevent="send">
      <input type="text" v-model="title" name="title" placeholder="Enter a long URL">
      <input type="submit" value="Create short URL" class="btn">
    </form>
  <div>
    <a :href="url" target="_blank">{{ url }}</a>
  </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Home",
  data() {
    return {
      title: '',
      url: ''
    }
  },
  methods: {
    send() {
      const url = {
        url: this.title
      };
      //in production remove the :5000 port 
    axios.post("/api", url).then(res => this.url = "http://" + window.location.hostname + ":5000/"+res.data)
    }
  }
}
</script>

<style scoped>

</style>
