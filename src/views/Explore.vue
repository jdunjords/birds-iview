<template>
  <v-container>

    <v-row class="text-center">
      <v-col id= "col-1">
        <ExploreCard/>
      </v-col>

      <v-col id= "col-2">
        <ExploreCard/>
      </v-col>

      <v-col id= "col-3">
        <ExploreCard/>
      </v-col>
    </v-row>

    <v-row class="text-center">
      <v-col id= "col-1">
        <ExploreCard/>
      </v-col>

      <v-col id= "col-2">
        <ExploreCard/>   
      </v-col>

      <v-col id= "col-3">
        <ExploreCard/>
      </v-col>
    </v-row>

    <v-row class="text-center">
      <v-col id= "col-1">
       <ExploreCard/>
      </v-col>

      <v-col id= "col-2">
      <ExploreCard/>       
      </v-col>

      <v-col id= "col-3">
      <ExploreCard/>    
      </v-col>
    </v-row>

  </v-container>
</template>

<script>
import ExploreCard from '../components/Explore-Card';

  export default {
    name: 'Explore',
    components: {
     ExploreCard,
    },

    data: () => ({
      
    }),
  }
</script>

<style scoped>

</style>

