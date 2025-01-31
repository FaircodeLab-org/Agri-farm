console.log("HERE")
frappe.pages["leaderboard"].refresh = (wrapper) => {
	console.log("ONLOAD LEADER BOARD")
    setTimeout(() => {
        cur_page.page.page.sidebar.find("li")[1].remove()
        cur_page.page.page.sidebar.find("li")[1].remove()
        cur_page.page.page.sidebar.find("li")[1].remove()
        cur_page.page.page.sidebar.find("li")[1].remove()
        cur_page.page.page.sidebar.find("li")[1].remove()
    },1000)

};
