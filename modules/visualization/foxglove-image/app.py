# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from typing import cast

from aws_cdk import App, CfnOutput, Environment

from stack import AppImagePublishingStack

# Project specific
project_name = os.getenv("SEEDFARMER_PROJECT_NAME")
deployment_name = os.getenv("SEEDFARMER_DEPLOYMENT_NAME")
module_name = os.getenv("SEEDFARMER_MODULE_NAME")

if len(f"{project_name}-{deployment_name}") > 36:
    raise ValueError(
        "This module cannot support a project+deployment name character length greater than 35"
    )


def _param(name: str) -> str:
    return f"SEEDFARMER_PARAMETER_{name}"


ecr_repo_name = os.getenv(_param("APP_ECR_REPOSITORY_NAME"), "")


app = App()


app_image_pushing_stack = AppImagePublishingStack(
    scope=app,
    id=f"{project_name}-{deployment_name}-{module_name}",
    project_name=cast(str, project_name),
    deployment_name=cast(str, deployment_name),
    repository_name=ecr_repo_name,
    module_name=cast(str, module_name),
    env=Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)


CfnOutput(
    scope=app_image_pushing_stack,
    id="metadata",
    value=app_image_pushing_stack.to_json_string(
        {
            "AppImageUri": app_image_pushing_stack.image_uri,
        }
    ),
)

app.synth()
