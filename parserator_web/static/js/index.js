/* TODO: Flesh this out to connect the form to the API and render results
   in the #address-results div. */
document.addEventListener('DOMContentLoaded', (e) => {
   const form = document.getElementById('form');
   const input = document.getElementById('address');


   form.addEventListener('submit', (e) => {
      e.preventDefault();
      const address = input.value

      /* complete fetch to backend */
      fetch(`/api/parse/?address=${address}`)
         .then(r => r.json())
         .then(parse_response => {
            addToDOM(parse_response)
         })
         .catch(error => {
            console.log('Error', error)
         })
      
      function addToDOM(parse_response){
         console.log(parse_response)
         div = document.getElementById('address-results')
         
         
         

         return
      }
      

   });
})


// Add error handling for front end, need to alert user of any error