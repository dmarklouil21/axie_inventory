const selectStatus = document.getElementById('status');

selectStatus.addEventListener('change', function(e) {
    if (selectStatus.value == 'Listed' || selectStatus.value == 'Sold') { 
        document.getElementById('sellingPrice').disabled = false;
        document.getElementById('sellingPrice').placeholder = 'Enter price';

        if (selectStatus.value == 'Sold') {
            document.getElementById('dateSold').disabled = false;
            document.getElementById('dateSold').required = true;
        }
        else {
            document.getElementById('dateSold').disabled = true;
            document.getElementById('dateSold').required = false;
        }
    }
    else {
        document.getElementById('sellingPrice').disabled = true;
        document.getElementById('sellingPrice').placeholder = 'NA';
        document.getElementById('dateSold').disabled = true;

        document.getElementById('sellingPrice').required = false;
        document.getElementById('dateSold').required = false;
    }
});