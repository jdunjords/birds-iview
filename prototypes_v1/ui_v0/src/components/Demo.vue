<template>
 <v-container>
    <v-row class="text-center">
      <v-col id = "col-1">  
          <v-card
          height= "550"
          width = "500"
          elevation="4"
          > 
            <v-img src="@/assets/default.png"
             max-height="400"
             max-width= "500"
            ></v-img>
  
           
            <div id= "fileInput">
              <h2 class="text-center"> Choose an Image  </h2> 
            <v-file-input
              accept="image/*"
              placeholder= "images"
              prepend-icon="mdi-camera-plus"
              multiple
              v-model= "myFile"
              >  
            </v-file-input>
            <v-btn class="button" v-on:click="onUpload"> UPLOAD </v-btn>
            </div>
        </v-card>
      </v-col>

      <v-spacer></v-spacer>

      <v-col id = "col-2">  
          <v-card
          height= "550"
          width = "500"
          elevation="4"
          id = "imageHolder"
          > 
            <div class = "recentUploads">
            <h2 class="text-center"> Recent Uploads </h2>  
          
              {{data}}
            </div>
          </v-card>
        
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';
export default {
    name: "Demo",
    data(){
        return {
            defaultImage: 'assets/default.png',
            myFile: null,
            data: null,
        }
    },
    methods: {
        onUpload(){
        var form = new FormData()
        var file = this.myFile[0];
        form.append('file', file)
         let config = {
            headers: {'Content-Type': 'multipart/form-data'}
          }
        console.log(file)
        axios.post('http://127.0.0.1:5000/upload/', form, config)
    
        }
    }
}
</script>

<style scoped>

.v-btn:not(.v-btn--round).v-size--default{
    width: 150px;
    height: 60px;
    font-size: 25px;
}
.main{
 background-color: pink;
 height: 1000px;
}

#fileInput{
    padding: 10px;
}
.recentUploads {
  padding: 20px;
}
.imageUpload {
   padding: 20px;
}
</style>