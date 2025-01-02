def schedule_tasks(config: Dict[str, Any]) -> None:
    def run_task(folder):
        print(f"Running scheduled task for folder: {folder}")
        folder_config = config.copy()
        folder_config["base_dir"] = folder
        organize_files(folder_config)

    daily = config.get("schedule", {}).get("daily", [])
    weekly = config.get("schedule", {}).get("weekly", [])
    custom = config.get("schedule", {}).get("custom", [])

    for folder in daily:
        schedule.every().day.at("02:00").do(run_task, folder=folder)

    for folder in weekly:
        schedule.every().sunday.at("02:00").do(run_task, folder=folder)

    for entry in custom:
        interval = getattr(schedule.every(), entry['interval'], None)
        if interval:
            interval.at(entry["time"]).do(run_task, folder=entry["folder"])
        else:
            print(f"Invalid interval: {entry['interval']}")

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Task scheduler interrupted. Exiting...")

