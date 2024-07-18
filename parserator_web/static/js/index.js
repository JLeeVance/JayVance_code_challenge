const results_div = document.getElementById('address-results');
const tBody = document.getElementById('results_table')
const form = document.getElementById('form');
const input = document.getElementById('address');


document.addEventListener('DOMContentLoaded', (e) => {
   
   form.addEventListener('submit', (e) => {
      e.preventDefault();
      results_div.style.display = 'none';
      tBody.innerHTML = '';
      const address = input.value
      
      /* complete fetch to backend */
      fetch(`/api/parse/?address=${address}`)
      .then(r => {
         if(!r.ok){
            return r.json().then(errorResponse => {
               throw new Error(errorResponse.ErrorMessage)
            })
         }
         return r.json();
      })
      .then(parse_response => {
         // console.log('After Good Fetch on Frontend',parse_response)
         
         addToDOM(parse_response)
      })
      .catch(error => {
         // console.log(error)
         showErrorMessages(error)
      })
   });
})

function createTableRows(addressComponents){
   console.log(addressComponents)
   for ([key, value] of Object.entries(addressComponents)){
      // console.log(key, value)
      const newRow = document.createElement('tr');
      const addressPart = document.createElement('td');
      const tag = document.createElement('td');
      
      addressPart.innerText = value;
      tag.innerText = key;
      newRow.appendChild(addressPart)
      newRow.appendChild(tag)
      tBody.appendChild(newRow)
   }
   return
}

function addToDOM(parse_response){
   const inputString = parse_response.input_string;
   const addressType = parse_response.address_type;
   const addressComponents = parse_response.address_components;

   const spanForType = document.getElementById('parse-type')
   
   if(spanForType){
      spanForType.innerHTML = addressType;
   }

   createTableRows(addressComponents)

   results_div.style = 'display:block'
   return
};

function showErrorMessages(error){
   const message = error.message
   //  Added div for user error data display
   const errorDiv = document.getElementById('error-div');
   const errorSpan = document.getElementById('error-message');

   errorSpan.textContent = message;
   errorDiv.style.display = 'block';

   setTimeout(() => {
      errorDiv.style.display = 'none';
      errorSpan.textContent = ''
   }, 3500);
}