(() => {
    HTMLElement.prototype.toggle = function(on) {
      switch(on) {
        case undefined:
          this.classList.toggle('hidden');
          break;
        case true:
          this.classList.remove('hidden');
          break;
        case false:
          this.classList.add('hidden');
          break;
        default:
          break;
      }
    }
  
    HTMLElement.prototype.hide = function() {
      this.toggle(false);
    }
  
    HTMLElement.prototype.show = function() {
      this.toggle(true);
    }
  
    const table = {
      checkboxes: document.querySelectorAll('.checkbox'),
      labelItemsSelected: document.getElementById('labelItemsSelected'),
      numberItemsSelected: 0,
      bulkActions: document.getElementById('bulkActions'),
      title: document.getElementById('title'),
    };
  
    let bulkActionsShown = table.numberItemsSelected > 0;
    console.log(`bulkActionsShown: ${bulkActionsShown}`);
  
    table.checkboxes.forEach((checkbox) => {
      checkbox.addEventListener('change', (event) => {
        table.numberItemsSelected = event.currentTarget.checked
          ? ++table.numberItemsSelected
          : --table.numberItemsSelected;
  
        table.labelItemsSelected.innerHTML = table.numberItemsSelected === 1
            ? `${table.numberItemsSelected} item selected`
            : `${table.numberItemsSelected} items selected`;
  
        bulkActionsShown = table.numberItemsSelected > 0;
        console.log(`bulkActionsShown: ${bulkActionsShown}`);
  
        if (bulkActionsShown) {
          table.bulkActions.show();
          table.title.hide();
        }
        else {
          table.bulkActions.hide();
          table.title.show();
        }
      });
    });
  })();
  