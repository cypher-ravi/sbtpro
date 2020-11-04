function remove(element) {
    element.parenetElement.remove(element);
}


document.getElementById('query').addEventListener('input', search)

function search() {
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: '/sbtadmin/search',
        data: {
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").attr("value"),
            query: $('#query').val(),
        },
        success: function(data) {
            // alert(data.obj);
            var element = document.querySelector('table.table');
            remove(element);

            data.obj = JSON.parse(data.obj);
            var tr = '';
            for (i in data.obj) {
                var tr = `${tr}
				<tr>
					<th scope="row">${data.obj[i].phone}</th>
					<td>${ data.obj[i].branch_name }</td>
					<td>${ data.obj[i].Mobile_No }</td>
					<td>${ data.obj[i].EmailId }</td>
					<td>${ data.obj[i].city }</td>
					<td><button class="btn btn-inverse-success">Edit</button></td>
					<td>Send Message</td>
				</tr>
				`
            }

            var html = `
				<table class="table mb-0">
					<thead class="thead-dark">
						<tr>
							<th scope="col">Branch user</th>
							<th scope="col">Name</th>
							<th scope="col">MobileNo.</th>
							<th scope="col">Email</th>
							<th scope="col">City</th>
							<th scope="col">Action</th>
							<th scope="col">Send Message</th>
						</tr>
					</thead>
					<tbody>
						${tr}
					</tbody>
				</table>
			`
            $('.table-responsive').append(html);
        },
    });
}