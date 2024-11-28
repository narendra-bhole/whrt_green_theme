import frappe

@frappe.whitelist()
def switch_theme(theme):
	if theme in ["Dark", "whrt_blue", "whrt_green"]:
		frappe.db.set_value("User", frappe.session.user, "whrt_theme", "whrt_green", theme)