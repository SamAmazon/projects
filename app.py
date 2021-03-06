#!/usr/bin/env python3

from aws_cdk import core

from projects.projects_stack import ProjectsStack


app = core.App()
ProjectsStack(app, "projects")

app.synth()
