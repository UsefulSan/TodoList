from django.contrib import admin

from goals.models import GoalCategory, Goal, GoalComment, Board, BoardParticipant


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


admin.site.register(GoalCategory, GoalCategoryAdmin)


class GoalAdmin(admin.ModelAdmin):
    list_display = ("user", "created", "updated", "title", 'description', 'due_date', 'status', 'priority', 'category')
    search_fields = ("title", "user")


admin.site.register(Goal, GoalAdmin)


class GoalCommentAdmin(admin.ModelAdmin):
    list_display = ("user", "created", "updated", 'text', 'goal')
    search_fields = ("user", 'goal')


admin.site.register(GoalComment, GoalCommentAdmin)


class BoardAdmin(admin.ModelAdmin):
    # list_display = ()
    search_fields = ("user", 'goal', 'title')


admin.site.register(Board, BoardAdmin)

admin.site.register(BoardParticipant, BoardAdmin)
