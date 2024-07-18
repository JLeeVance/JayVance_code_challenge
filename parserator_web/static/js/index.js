/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
document.addEventListener('DOMContentLoaded', (e) => {
   const form = document.getElementById('form');
   const button = document.getElementById('submit');
   const input = document.getElementById('address');


   form.addEventListener('submit', (e) => {
      e.preventDefault();
      // console.log(e)
      const address = input.value
      console.log(address)

      fetch(`/api/parse/?address=${address}`)
         .then(r => r.json())
         .then(addressComponents => {
            console.log(addressComponents)
         })
         .catch(error => {
            console.log('Error', error)
         })
      
      function addToDOM(addressComponents){
         return
      }
      

   });
})
