<template>
  <v-container>
    <v-row class="text-center">


    <!-- home paragraph and image -->   
      <v-col id = "col-1">  
        <h1 > What is pEEp? </h1>
      <p> 
      <br>
       David Plemmons, bird enthusiast and entrepreneur, 
       has been working over the last 3 years to bring the bird-enthusiast 
       community even closer together by creating a bird feeder with an 
      integrated camera that allows you to view birds from a live stream video. 
      <br> <br>
      David's plan is to educate people on the importance of bird-watching and
       bird indentification. From a scientific perspective, the identification 
       of individual birds would present avian researchers with a completely 
       new dimension of data. This would allow researchers to better study trends
        within different bird populations. 
      <br> <br>
      Team Bird's iView is going to expand David's idea and create an AI model that
       will be able to identify specific species of birds from the images captured 
       by the pEEp bird feeder. Additionally, we will be creating an easy way to share 
       user findings which will allow users to connect with other members of the bird
      community.  </p>
      
      <!-- <v-img src="@/assets/default.png"
             max-height="400"
             max-width= "500"
            ></v-img> -->
      </v-col>


     <!-- Login box component-->
        <v-col id = "col-2">  
          <Login/>
        </v-col>
     </v-row>
  </v-container>
</template>

<script>
  import Login from '../components/Login-Box';

  export default {
    name: 'Home',
    components: {
      Login,
     
    },

    data: () => ({
      
    }),
  }
</script>

<style scoped>

</style>

