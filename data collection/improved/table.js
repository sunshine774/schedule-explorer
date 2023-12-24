// Find the table element
var table = document.querySelector("#gridview-1160-body"); // Note you can change '#gridview-1160-body' with '#panel-1180-innerCt' to include the whole table, but the one already in the script is optimal.

// Check if the table is found
if (table) {
  // Get all cells in the table
  var cells = table.querySelectorAll("td");

  // Concatenate cell contents with newlines and log as a single output
  var tableContent = Array.from(cells).map(function(cell) {
    return cell.textContent.trim();
  }).join('\n');

  console.log(tableContent);
} else {
  console.log("Table not found");
}
