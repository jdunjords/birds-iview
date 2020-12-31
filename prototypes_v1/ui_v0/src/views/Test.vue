<template>
  <v-container>
      <v-row class= "text-center">
          <v-col id= "col-1">
            <ImageUpload/>
          </v-col>

      </v-row>
  </v-container>
</template>

<script>
import ImageUpload from '../components/Image-Upload';

  export default {
    name: 'Test',
    components: {
     ImageUpload,
    },

    data: () => ({
      
    }),
  }
</script>

<style scoped>

</style>

