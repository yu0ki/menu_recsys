const formFieldsDiv = document.getElementById("form-fields");
const addFieldBtn = document.getElementById("add-field-btn");
const dishField = document.getElementsByClassName("dish-field");
const buttons = document.querySelectorAll(".remove-field-btn");

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

    // 削除ボタンにOnClickリスナーをつける
    remove_button = newField.getElementsByClassName("remove-field-btn")[0]
    remove_button.addEventListener(
        'click', () => {
            // ボタンが所属するアイテムの削除
            const item = remove_button.closest('.dish-field');
            item.remove();
        }
    )


  fieldCount++;
  formFieldsDiv.appendChild(newField);
});

buttons.forEach(remove_button => {
    remove_button.addEventListener('click', () => {
      // ボタンが所属するアイテムの削除
      const item = remove_button.closest('.dish-field');
      item.remove();
    });
  });