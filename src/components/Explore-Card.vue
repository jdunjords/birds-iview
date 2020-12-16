<template>
  <v-container>
   
    <v-card
            width = "320"
            height = "300"
            elevation = "6"
            margin = "0"
           
           > 
           <v-card-title> 
             <v-icon left> mdi-account-circle </v-icon>
             user 1 </v-card-title>
           <v-img src="@/assets/default.png"
             max-height="400"
             max-width= "500"
            ></v-img>
            <div class = "icons">
            <v-icon left> mdi-cards-heart </v-icon>
            <v-icon left> mdi-comment </v-icon>
            <v-icon left> mdi-flag </v-icon>

            </div>

           </v-card>


  </v-container>
</template>

<script>


  export default {
    name: 'ExploreCard',
    components: {
     
    },

    data: () => ({
      
    }),
  }
</script>

<style scoped>
.icons{
  padding: 10px;
  float: left;
}
.flag{
  float: right !important ;
}
</style>

