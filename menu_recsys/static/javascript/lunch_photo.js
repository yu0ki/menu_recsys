const formFieldsDiv = document.getElementById("form-fields");
const addFieldBtn = document.getElementById("add-field-btn");
const removeFieldBtn = document.getElementById("remove-field-btn");
const dishField = document.getElementsByClassName("dish-field");

let fieldCount = 0;

addFieldBtn.addEventListener("click", () => {
  const newField = dishField[0].cloneNode(true);
  newField.setAttribute("name", "new" + fieldCount.toString());
  

  // Add unique ID to each field to ensure proper form submission
  Array.from(newField.children).forEach((el) => {
    const elName = el.getAttribute("name");
    if (elName) {
      el.setAttribute("name", `${elName}_${fieldCount}`);
    }
  });

  fieldCount++;
  formFieldsDiv.appendChild(newField);
});

removeFieldBtn.addEventListener("click", () => {
  if (fieldCount > 0) {
    formFieldsDiv.lastElementChild.remove();
    fieldCount--;
  }
});