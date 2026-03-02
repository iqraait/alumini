from django.core.management.base import BaseCommand
import pandas as pd
from mainapp.models import Department  # Change this to your actual app name


class Command(BaseCommand):
    help = "Import departments from Excel file"

    def handle(self, *args, **kwargs):
        file_path = "/home/ot/Desktop/alumini form/dep.xlsx"  # Update this path

        # Read the Excel file
        df = pd.read_excel(file_path)

        created = 0
        skipped = 0

        for _, row in df.iterrows():
            dept_name = str(row["DEPARTMENT"]).strip()

            # Skip the header if it's included
            if dept_name.upper() == "DEPARTMENT":
                continue

            try:
                # Try to get existing department
                dept, is_created = Department.objects.get_or_create(
                    name=dept_name,
                    defaults={"name": dept_name}
                )

                if is_created:
                    created += 1
                    self.stdout.write(
                        self.style.SUCCESS(f"✅ Created: {dept_name}")
                    )
                else:
                    skipped += 1
                    self.stdout.write(
                        self.style.WARNING(f"⏭️  Already exists: {dept_name}")
                    )

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"❌ Error with {dept_name}: {str(e)}")
                )
                skipped += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\n🎉 Finished | Created: {created} | Already existed: {skipped}"
            )
        )