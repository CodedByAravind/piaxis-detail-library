ALTER TABLE details ENABLE ROW LEVEL SECURITY;
ALTER TABLE details FORCE ROW LEVEL SECURITY;

CREATE POLICY admin_all_access
ON details
FOR SELECT
USING (
    current_setting('app.user_role') = 'admin'
);

CREATE POLICY architect_limited_access
ON details
FOR SELECT
USING (
    current_setting('app.user_role') = 'architect'
    AND source IN ('standard', 'user_project')
);
