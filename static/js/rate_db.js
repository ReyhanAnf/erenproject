//   // Import the functions you need from the SDKs you need
//   import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.3/firebase-app.js";
//   import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.3/firebase-analytics.js";
//   import { getDatabase, ref, set ,get ,child, update, remove } from "https://www.gstatic.com/firebasejs/9.6.3/firebase-database.js";
//   // TODO: Add SDKs for Firebase products that you want to use
//   // https://firebase.google.com/docs/web/setup#available-libraries

//   // Your web app's Firebase configuration
//   // For Firebase JS SDK v7.20.0 and later, measurementId is optional
//   const firebaseConfig = {
//     apiKey: "AIzaSyBo0Nvbs5rnah9_0DaM8_R25uXOMXMg9aA",
//     authDomain: "rate-pn.firebaseapp.com",
//     databaseURL: "https://rate-pn-default-rtdb.asia-southeast1.firebasedatabase.app",
//     projectId: "rate-pn",
//     storageBucket: "rate-pn.appspot.com",
//     messagingSenderId: "187866711518",
//     appId: "1:187866711518:web:a1df82b6651c0b9ceb494f",
//     measurementId: "G-MNCNTJXW1R"
//   };

//   // Initialize Firebase
//   const app = initializeApp(firebaseConfig);
//   const analytics = getAnalytics(app);










// //################################################
// //###### Out Data #############################
// //################################################

// const db = getDatabase()


// function outData(id){
//   const dbref = ref(db);
  
  
//   get(child(dbref, 'RATING/'+ id)).then((snapshot)=>{
//     if(snapshot.exists()){
//       let data = {'Nama':'','Rate':0,'Message':''};
  
//       data['Nama'] += snapshot.val().NAMA;
//       data['Rate'] += snapshot.val().RATE;
//       data['Message'] += snapshot.val().MESSAGE;
      
//       console.log(data)
      
//     }else{
//       alert('Data Tidak Terdeteksi/Ada');
//     }
//   })
//   .catch((error)=>{
//     console.log('error')
//   })

  
// }



// function outDataAll(){
//   const dbref = ref(db);
  
  
//   get(child(dbref, 'RATING/')).then((snapshot)=>{
//     if(snapshot.exists()){
//       let data = snapshot.val();
      
//       console.log(data)
      
//     }else{
//       alert('Data Tidak Terdeteksi/Ada');
//     }
//   })
//   .catch((error)=>{
//     console.log('error')
//   })
  
// }



// function outGraphRate(){
//   const dbref = ref(db);
  
  
  
//   get(child(dbref, 'RATING/')).then((snapshot)=>{
//     if(snapshot.exists()){
//       let dataa = snapshot.val().length;
//       let star1 = 0;
//       let star2 = 0;
//       let star3 = 0;
//       let star4 = 0;
//       let star5 = 0;
      
      
//       for(let i = 0;i < dataa;i++){
//         if(snapshot.val()[i]['RATE']< 1.5){
//           star1 += 1;
//         }else if(snapshot.val()[i]['RATE'] < 2.5){
//           star2 += 1;
//         }else if(snapshot.val()[i]['RATE'] < 3.5){
//           star3 += 1;
//         }else if(snapshot.val()[i]['RATE'] < 4.5){
//           star4 += 1;
//         }else if(snapshot.val()[i]['RATE'] < 10.1){
//           star5 += 1;
//         }else{
//           console.log(snapshot.val()[i]['RATE'])
//         }
        
//       }
      
//       //alert(star1 +star2+star3+star4+star5);
      
//       new Chart(document.getElementById("rting"), {
//         type: 'bar',
//         data: {
//           labels: ["5⭐", "4⭐", "3⭐", "2⭐", "1⭐"],
//           datasets: [
//             {
//               axis : 'y',
//               label: "Value",
//               backgroundColor: [
//                     'rgba(75, 192, 192, 0.4)',
//                     'rgba(54, 162, 235, 0.4)',
//                     'rgba(255, 205, 86, 0.4)',
//                     'rgba(255, 99, 132, 0.4)',
//                     'rgba(255, 159, 64, 0.4)'
//                 ],
//                 borderColor: [
//                     'rgb(75, 192, 192)',
//                     'rgb(54, 162, 235)',
//                     'rgb(255, 205, 86)',
//                     'rgb(255, 99, 132)',
//                     'rgb(255, 159, 64)'
//                 ],
//               borderWidth: 1,
//               data : [star5, star4, star3, star2, star1]
//               }
//             ]
//         },
//         options: {
//           legend: { display: false },
//           title: {
//             display: true,
//             text: 'Rating'
//           },
//           indexAxis: 'y',
//           elements: {
//             bar: {
//               borderWidth: 1,
//             }
//           }
//         }
//       });
      
      
//     }else{
//       alert('Data Tidak Terdeteksi/Ada');
//     }
//   })
//   .catch((error)=>{
//     console.log('error')
//   })
  
// }


// //################################################
// //###### Insert Data #############################
// //################################################

// let jumlah = 0;

// function inputData(){
  
//   let id = 0;
//   const dbref = ref(db);
  
//   get(child(dbref, 'RATING/')).then((snapshot)=>{
    
//     if(snapshot.exists()){
      
//       id = snapshot.val().length;
      
//       jumlah = id;
      
//       let nama = document.querySelector('.rn').value;
//       let rate = document.querySelector('.valrate').value;
//       let message = document.querySelector('.ulas').value;
      
//       set(ref(db, 'RATING/' + id), {
//           NAMA: name,
//           RATE: rate,
//           MESSAGE: message
//         })
//         .then(() => {
//           alert('Terkirim!');
//         })
//         .catch((error) => {
//           alert('Maaf gan error :' + error)
//         });
      
//     }else{
      
//       alert('ada yang salah')
      
//     }
    
//   })
//   .catch((error)=>{
    
//     alert(error)
    
//   })
  
// }


// let kirim = document.querySelector('.kirim');

// kirim.addEventListener('click',()=>{
//   inputData()
// })

// outGraphRate()