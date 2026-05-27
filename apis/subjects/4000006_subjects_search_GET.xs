query subjects verb=GET {
    api_group = "subjects"

    input { }

    stack {
        db.query subject {
            where = $db.subject.user_id == $auth.id && $db.subject.name ilike "%" ~ $input.search_term ~ "%"
            return = {type: "list"}
        } as $name_matched_subjects

        db.query academic_tasks {
            where = $db.academic_tasks.user_id == $auth.id
            return = {type: "list"}
        } as $all_tasks

        function.run "filter_overdue_tasks" {
            input = {
                tasks: $all_tasks
            }
        } as $overdue_subject_ids

        db.query subject {
            where = $db.subject.user_id == $auth.id && $db.subject.id in $overdue_subject_ids
            return = {type: "list"}
        } as $overdue_subjects

        var $merged_subjects {
    value = $name_matched_subjects|merge:$overdue_subjects|unique
}
    }

    response = $merged_subjects
}