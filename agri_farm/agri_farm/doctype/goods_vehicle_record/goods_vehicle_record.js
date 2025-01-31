// Copyright (c) 2023, Momscode Technologies and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Period Of Work', {
//     date_and_time_finished__work: function(frm, cdt, cdn) {
//         // Get the current child table row
//         let row = locals[cdt][cdn];

//         // Ensure both fields are in valid datetime format
//         let commenced_work = row.date_and_time_commenced_work ? moment(row.date_and_time_commenced_work) : null;
//         let finished_work = row.date_and_time_finished__work ? moment(row.date_and_time_finished__work) : null;

//         // Check if both fields have valid values
//         if (commenced_work && finished_work) {
//             // Calculate the time difference in seconds
//             let time_diff_in_seconds = finished_work.diff(commenced_work, 'seconds');

//             if (time_diff_in_seconds >= 0) {
//                 // Convert seconds to hours and minutes
//                 let hours = Math.floor(time_diff_in_seconds / 3600);
//                 let minutes = Math.floor((time_diff_in_seconds % 3600) / 60);

//                 // Format as "X hours Y minutes"
//                 let formatted_time = `${hours} hours ${minutes} minutes`;

//                 // Set the total_time_worked field in the child table row
//                 frappe.model.set_value(cdt, cdn, 'total_time_worked', formatted_time);
//             } else {
//                 // If finished work time is earlier than commenced work time, show an error
//                 frappe.msgprint(__('The finished work time cannot be earlier than the commenced work time.'));
//                 frappe.model.set_value(cdt, cdn, 'total_time_worked', null);
//             }
//         } else {
//             // Clear total_time_worked if either field is empty
//             frappe.model.set_value(cdt, cdn, 'total_time_worked', null);
//         }
//     }
// });
