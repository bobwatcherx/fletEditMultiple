from flet import *

def main(page:Page):

	page.theme_mode = "light"

	you_edit = Column()

	# NOW CREATE DATA ARRAY LIKE  NAME AND AGE

	mydata = [
		{"name":"boy","age":12,"select":False},
		{"name":"jjang","age":22,"select":False},
		{"name":"girl","age":33,"select":False},
		{"name":"ddw","age":66,"select":False},
	]

	# NOW CREATE TABLE 
	mytable = DataTable(
		show_checkbox_column=True,
		columns=[
			DataColumn(Text("name")),
			DataColumn(Text("age")),
			DataColumn(Text("select")),
			],
		rows=[]
		)

	# SAVE AND CLOSE DIALOG EDiT
	def savedata(e):
		# NOW SAVE IF YOU CLICK SAVE BUTTON IN DIALOG EDIT
		for data_edit in you_edit.controls:
			for m in mydata:
				# AND CHECK IF NAME IN MYDATA IS EQUAL in you_edit
				# THIS CHECK NAME 
				if m['name'] == data_edit.content.controls[0].value:
					# IF VALID THEN UPDATE DATA IN MYDATA FROM you_edit
					# THIS data_edit.content.controls[1].value IS FROM TEXTFIELD NAME
					m['name'] = data_edit.content.controls[1].value
					# AND UPdATE FORM AGE
					m['age'] = data_edit.content.controls[2].value
			
		# AFTER THAT THEN REFRESH DATA TABLE AND LOAD TABLE AGAIN
		mytable.rows.clear()
		load_table()

		# AND CLose dialog_edit
		dialog_edit.open = False
		# AND REMOVE LIST FORM EDIT you_edit
		you_edit.controls.clear()
		page.update()	


	# NOW CRATE DIALOG EDiT IF YOU CLICK BUTTON EDiT NOW
	# THEN SHOW DIALOG 
	dialog_edit = AlertDialog(
		title=Text("edit you"),
		content=Column([
			# ANDD you_edit IN HERE
			you_edit 
			],scroll="always"),
		actions=[
			ElevatedButton("Save",
				on_click=savedata
				)
			],
		actions_alignment="end"
		)

	# REMOVE YOU SELECT FROM you_edit
	def remove_this(e):
		# NOW IF I CLICK CLOSE RED ICON THEN REMOVE THE 
		# Container
		# NOW CHECK IF you_edit if HAVE DATA
		if len(you_edit.controls) > 0:
			for i,d in enumerate(you_edit.controls):
				# THIS SCRIPT IS CHECK IF NAME IS SAME IF NOT THEN NOT REMOVE

				if d.content.controls[1].value ==  e.control.data.controls[0].value:
					# THEN REMOVE INDEX WITH POP
					you_edit.controls.pop(i)
		page.update()


	def opendialog_edit(e):
		# dialog_edit WILL OPEN IF THERE DATA IN you_edit
		# IF NOT THEN SHOW SNACK BAR YOU DONT HAVE you_edit data
		if len(you_edit.controls) > 0:
			# SHOW DIALOG
			page.dialog = dialog_edit
			dialog_edit.open = True
			page.update()
		else:
			page.snack_bar = SnackBar(
				Text("YOU NO HAVE DATA FOR SELECT",size=30),
				bgcolor="red"
				)
			page.snack_bar.open = True
			page.update()
		page.update()


	# RUN FUNCTION IF YOU CEK AND UNCHECK CHECKBOX
	def myselect(e):
		# NOW RUN APPEND IF STATUS CHECKBOX IS TRUE
		if e.control.value == True:
			# NOW GET NAME AND AGE YoU SELECT
			add_name = e.control.data.controls[0].value
			add_age = e.control.data.controls[1].value

			# NOW PUSH NAME AND AGE TO you_edit
			you_edit.controls.append(
				Container(
					bgcolor="blue200",
					padding=10,
					content=Column([
						Text(add_name,size=30),
						# AND CREATE TEXTFELD
						TextField(value=add_name),
						# FROM HERE GUYS INDEX IS 2
						TextField(value=add_age),
						# AND CREATE ICONBUTTON CLOSE
						# IF YOU REMOVE TEXTFIELD IN you_edit
						IconButton(icon="close",
							icon_color="red",
							icon_size=40,
							# AND ADD NAME TEXTFIELD AND AGE TEXTFIELD TO DATA PROPERTY
							data=Row([
								Text(add_name),
								Text(add_name),
								]),
							# AND ADD ON CLICK FOR RUN REMOVE LIST 
							on_click=remove_this
							)
						])
					)

				)
		page.update()




	# NOW INSERT mydata TO mytable
	def load_table():
		for x in mydata:
			mytable.rows.append(
				DataRow(
					cells=[
					DataCell(Text(x['name'])),
					DataCell(Text(x['age'])),
					DataCell(
						# AND CREATE CHECKBOX FOR select
						Checkbox(value=x['select'],
							fill_color="blue",
							# AND ADD name AND AGE TO DATA PROPERTY
							data=Row([
								Text(x['name']),
								Text(x['age']),
								]),
							# AND CREATE FUNCTION IF YOU CHANGE CHECKBOX CEK OR UNCHECK
							on_change=myselect
							)
						),
					]
					)
				)
	load_table()

	page.add(
		Column([
		Text("Edit Multiple table",size=30,weight="bold"),
		mytable,
		# CREATE BUTTON Edit
		ElevatedButton("Edit now",
			on_click=opendialog_edit
			)

			])


		)
flet.app(target=main)
