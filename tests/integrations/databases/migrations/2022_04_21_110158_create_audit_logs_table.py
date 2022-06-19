"""CreateAuditLogsTable Migration."""

from masoniteorm.migrations import Migration


class CreateAuditLogsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("audit_logs") as table:
            table.increments("id")
            table.integer("editor_id").unsigned().nullable()
            table.integer("model_id").unsigned()
            table.string("model_name")
            table.string("action")
            table.json("columns").default("{}")
            table.json("old_value").default("{}")
            table.json("new_value").default("{}")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("audit_logs")
